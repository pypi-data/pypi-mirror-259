import numpy as np
import traceback
from napari_pixseq.funcs.pixseq_utils_compute import Worker
import time
import os
from multiprocessing import shared_memory
from picasso import localize
from picasso.localize import get_spots, identify_frame
from picasso.gaussmle import gaussmle
from functools import partial
import concurrent.futures
import multiprocessing


def remove_overlapping_locs(locs, box_size):

    try:

        coordinates = np.vstack((locs.y, locs.x)).T

        # Calculate all pairwise differences
        diff = coordinates[:, np.newaxis, :] - coordinates[np.newaxis, :, :]

        # Calculate squared distances
        dist_squared = np.sum(diff ** 2, axis=-1)

        # Check if the array is of integer type
        if coordinates.dtype.kind in 'iu':
            # Use the maximum integer value for the diagonal if the array is of integer type
            max_int_value = np.iinfo(coordinates.dtype).max
            np.fill_diagonal(dist_squared, max_int_value)
        else:
            # Use infinity for the diagonal if the array is of float type
            np.fill_diagonal(dist_squared, np.inf)

        # Identify overlapping coordinates (distance less than X)
        overlapping = np.any(dist_squared < box_size ** 2, axis=1)

        non_overlapping_locs = locs[~overlapping]
        non_overlapping_locs = np.array(non_overlapping_locs).view(np.recarray)

    except:
        pass

    return non_overlapping_locs


def cut_spots(movie, ids_frame, ids_x, ids_y, box):

    n_spots = len(ids_x)
    r = int(box / 2)
    spots = np.zeros((n_spots, box, box), dtype=movie.dtype)
    for id, (frame, xc, yc) in enumerate(zip(ids_frame, ids_x, ids_y)):
        spots[id] = movie[frame, yc - r : yc + r + 1, xc - r : xc + r + 1]

    return spots


def picasso_detect(dat):

    result = None

    try:

        frame_index = dat["frame_index"]
        min_net_gradient = dat["min_net_gradient"]
        box_size = dat["box_size"]
        roi = dat["roi"]
        dataset = dat["dataset"]
        channel = dat["channel"]
        detect = dat["detect"]
        fit = dat["fit"]
        remove_overlapping = dat["remove_overlapping"]
        stop_event = dat["stop_event"]

        if not stop_event.is_set():

            # Access the shared memory
            shared_mem = shared_memory.SharedMemory(name=dat["shared_memory_name"])
            np_array = np.ndarray(dat["shape"], dtype=dat["dtype"], buffer=shared_mem.buf)

            # Perform preprocessing steps and overwrite original image
            frame = np_array[frame_index].copy()

            if detect:
                locs = identify_frame(frame, min_net_gradient, box_size, 0, roi=roi)

                if remove_overlapping:
                    # overlapping removed prior to fitting to increase speed
                    locs = remove_overlapping_locs(locs, box_size)

            else:
                locs = dat["frame_locs"]

            expected_loc_length = 4

            if fit:
                expected_loc_length = 12
                try:
                    image = np.expand_dims(frame, axis=0)
                    camera_info = {"baseline": 100.0, "gain": 1, "sensitivity": 1.0, "qe": 0.9, }
                    spot_data = get_spots(image, locs, box_size, camera_info)

                    # frame = np.expand_dims(frame, axis=0)
                    # locs.frame = 0
                    # spot_data = cut_spots(frame, locs.frame, locs.x, locs.y, box_size)

                    theta, CRLBs, likelihoods, iterations = gaussmle(spot_data, eps=0.001, max_it=1000, method="sigma")
                    locs = localize.locs_from_fits(locs.copy(), theta, CRLBs, likelihoods, iterations, box_size)

                    locs.frame = frame_index

                    if remove_overlapping:
                        # sometimes locs can overlap after fitting
                        locs = remove_overlapping_locs(locs, box_size)

                except:
                    # print(traceback.format_exc())
                    pass

            for loc in locs:
                loc.frame = frame_index

            render_locs= {}
            render_locs[frame_index] = np.vstack((locs.y, locs.x)).T.tolist()

            locs = [loc for loc in locs if len(loc) == expected_loc_length]
            locs = np.array(locs).view(np.recarray)

            result = {"dataset": dataset, "channel": channel, "frame_index": frame_index,
                      "locs": locs,"render_locs": render_locs}

    except:
        print(traceback.format_exc())
        pass

    return result


class _picasso_detect_utils:



    def populate_localisation_dict(self, loc_dict, render_loc_dict, detect_mode, image_channel, box_size, fitted=False):

        if self.verbose:
            print("Populating localisation dictionary...")

        detect_mode = detect_mode.lower()

        try:

            for dataset_name, locs in loc_dict.items():

                render_locs = render_loc_dict[dataset_name]

                if detect_mode == "fiducials":

                    loc_centres = self.get_localisation_centres(locs)

                    fiducial_dict = {"localisations": [], "localisation_centres": [], "render_locs": {}}

                    fiducial_dict["localisations"] = locs.copy()
                    fiducial_dict["localisation_centres"] = loc_centres.copy()
                    fiducial_dict["render_locs"] = render_locs

                    fiducial_dict["fitted"] = fitted
                    fiducial_dict["box_size"] = box_size

                    if dataset_name not in self.localisation_dict["fiducials"].keys():
                        self.localisation_dict["fiducials"][dataset_name] = {}
                    if image_channel not in self.localisation_dict["fiducials"][dataset_name].keys():
                        self.localisation_dict["fiducials"][dataset_name][image_channel.lower()] = {}

                    self.localisation_dict["fiducials"][dataset_name][image_channel.lower()] = fiducial_dict.copy()

                else:

                    loc_centres = self.get_localisation_centres(locs)

                    self.localisation_dict["bounding_boxes"]["localisations"] = locs.copy()
                    self.localisation_dict["bounding_boxes"]["localisation_centres"] = loc_centres.copy()
                    self.localisation_dict["bounding_boxes"]["fitted"] = fitted
                    self.localisation_dict["bounding_boxes"]["box_size"] = box_size


        except:
            print(traceback.format_exc())
            self.picasso_progressbar.setValue(0)
            self.picasso_detect.setEnabled(True)
            self.picasso_fit.setEnabled(True)
            self.picasso_detectfit.setEnabled(True)

    def _picasso_wrapper_result(self, result):

        try:

            if self.verbose:
                print("Picasso wrapper result received")

            fitted, loc_dict, render_loc_dict, total_locs = result

            detect_mode = self.picasso_detect_mode.currentText()
            image_channel = self.picasso_channel.currentText()
            box_size = int(self.picasso_box_size.currentText())

            dataset_names = list(loc_dict.keys())

            if len(dataset_names) > 0:

                self.populate_localisation_dict(loc_dict, render_loc_dict, detect_mode,
                    image_channel, box_size, fitted)

                if fitted:
                    print("Fitted {} localisations".format(total_locs))
                else:
                    print("Detected {} localisations".format(total_locs))

        except:
            print(traceback.format_exc())

    def _picasso_wrapper_finished(self):

        try:

            image_channel = self.picasso_channel.currentText()
            dataset_name = self.picasso_dataset.currentText()

            if dataset_name == "All Datasets":
                dataset_name = self.active_dataset

            self.update_active_image(channel=image_channel.lower(), dataset=dataset_name)

            self.draw_bounding_boxes()

            self.update_ui()

        except:
            print(traceback.format_exc())

    def get_frame_locs(self, dataset_name, image_channel, frame_index):

        try:

            loc_dict, n_locs, _ = self.get_loc_dict(dataset_name,
                image_channel.lower(), type = "fiducials")

            if "localisations" not in loc_dict.keys():
                return None
            else:
                locs = loc_dict["localisations"]
                locs = locs[locs.frame == frame_index]

                return locs.copy()

        except:
            print(traceback.format_exc())
            return None

    def _picasso_wrapper(self, progress_callback, detect, fit, min_net_gradient, image_channel):

        loc_dict = {}
        render_loc_dict = {}
        total_locs = 0
        try:

            box_size = int(self.picasso_box_size.currentText())
            dataset_name = self.picasso_dataset.currentText()
            frame_mode = self.picasso_frame_mode.currentText()
            remove_overlapping = self.picasso_remove_overlapping.isChecked()
            roi = self.generate_roi()

            if dataset_name == "All Datasets":
                dataset_list = list(self.dataset_dict.keys())
            else:
                dataset_list = [dataset_name]

            channel_list = [image_channel.lower()]

            self.shared_images = self.create_shared_images(dataset_list=dataset_list, channel_list=channel_list)

            compute_jobs = []

            if self.verbose:
                print("Creating Picasso compute jobs...")

            if self.verbose:
                print("Creating compute jobs for {} datasets...".format(len(self.shared_images)))

            for image_dict in self.shared_images:

                image_dict = image_dict.copy()

                if frame_mode.lower() == "active":
                    frame_list = [self.viewer.dims.current_step[0]]
                else:
                    n_frames = image_dict['shape'][0]
                    frame_list = list(range(n_frames))

                for frame_index in frame_list:

                    time_start = time.time()

                    if self.verbose:
                        print("Creating compute job for frame {}".format(frame_index))

                    frame_locs = self.get_frame_locs(image_dict["dataset"],
                        image_channel, frame_index)

                    if detect == False and frame_locs is None:
                        continue
                    else:
                        compute_job = {"dataset": image_dict["dataset"],
                                       "channel": image_dict["channel"],
                                       "frame_index": frame_index,
                                       "shared_memory_name": image_dict['shared_memory_name'],
                                       "shape": image_dict['shape'],
                                       "dtype": image_dict['dtype'],
                                       "detect": detect,
                                       "fit": fit,
                                       "min_net_gradient": int(min_net_gradient),
                                       "box_size": int(box_size),
                                       "roi": roi,
                                       "frame_locs": frame_locs,
                                       "remove_overlapping": remove_overlapping,
                                       "stop_event": self.stop_event,
                                       }

                    compute_jobs.append(compute_job)

                    if self.verbose:
                        time_end = time.time()
                        time_duration = time_end - time_start
                        print("Compute job created in {} seconds".format(time_duration))

            if len(compute_jobs) > 0:

                if self.verbose:
                    print(f"Starting Picasso {len(compute_jobs)} compute jobs...")

                timeout_duration = 10  # Timeout in seconds

                loc_dict = {}
                render_loc_dict = {}

                if frame_mode.lower() == "active":
                    executor_class = concurrent.futures.ThreadPoolExecutor
                    cpu_count = 1
                else:
                    executor_class = concurrent.futures.ProcessPoolExecutor
                    cpu_count = int(multiprocessing.cpu_count() * 0.9)

                with executor_class(max_workers=cpu_count) as executor:
                    futures = {executor.submit(picasso_detect, job): job for job in compute_jobs}

                iter = 0
                for future in concurrent.futures.as_completed(futures):
                    if self.stop_event.is_set():
                        future.cancel()
                    else:
                        job = futures[future]
                        try:
                            result = future.result(timeout=timeout_duration)  # Process result here

                            if result is not None:
                                dataset_name = result["dataset"]

                                if dataset_name not in loc_dict:
                                    loc_dict[dataset_name] = []
                                    render_loc_dict[dataset_name] = {}

                                locs = result["locs"]
                                render_locs = result["render_locs"]

                                loc_dict[dataset_name].extend(locs)
                                render_loc_dict[dataset_name] = {**render_loc_dict[dataset_name], **render_locs}

                            iter += 1
                            progress = int((iter / len(compute_jobs)) * 100)
                            progress_callback.emit(progress)  # Emit the signal

                        except concurrent.futures.TimeoutError:
                            # print(f"Task {job} timed out after {timeout_duration} seconds.")
                            pass
                        except Exception as e:
                            print(f"Error occurred in task {job}: {e}")  # Handle other exceptions
                            pass

                if self.verbose:
                    print("Finished Picasso compute jobs...")
                    print("Compiling Picasso results...")

                total_locs = 0
                for dataset, locs in loc_dict.items():
                    locs = np.hstack(locs).view(np.recarray).copy()
                    locs.sort(kind="mergesort", order="frame")
                    locs = np.array(locs).view(np.recarray)
                    loc_dict[dataset] = locs
                    total_locs += len(locs)

            self.restore_shared_images()
            self.update_ui()

        except:
            print(traceback.format_exc())
            self.restore_shared_images()

            self.update_ui()

            loc_dict = {}
            render_loc_dict = {}
            total_locs = 0

        return fit, loc_dict, render_loc_dict, total_locs

    def pixseq_picasso(self, detect = False, fit = False):

        try:
            if self.dataset_dict != {}:

                min_net_gradient = self.picasso_min_net_gradient.text()
                image_channel = self.picasso_channel.currentText()

                if min_net_gradient.isdigit() and image_channel != "":

                    self.picasso_progressbar.setValue(0)
                    self.picasso_detect.setEnabled(False)
                    self.picasso_fit.setEnabled(False)
                    self.picasso_detectfit.setEnabled(False)

                    self.update_ui(init=True)

                    self.worker = Worker(self._picasso_wrapper,
                        detect=detect, fit=fit,
                        min_net_gradient=min_net_gradient,
                        image_channel=image_channel,)

                    self.worker.signals.progress.connect(partial(self.pixseq_progress, progress_bar=self.picasso_progressbar))
                    self.worker.signals.result.connect(self._picasso_wrapper_result)
                    self.worker.signals.finished.connect(self._picasso_wrapper_finished)
                    self.worker.signals.error.connect(self.update_ui)
                    self.threadpool.start(self.worker)


        except:
            print(traceback.format_exc())

            self.update_ui()


    def generate_roi(self):

        if self.verbose:
            print("Generating ROI")

        border_width = self.picasso_roi_border_width.text()
        window_cropping = self.picasso_window_cropping.isChecked()

        roi = None

        try:

            generate_roi = False

            if window_cropping:
                layers_names = [layer.name for layer in self.viewer.layers if layer.name not in ["bounding_boxes", "fiducials"]]

                crop = self.viewer.layers[layers_names[0]].corner_pixels[:, -2:]
                [[y1, x1], [y2, x2]] = crop

                generate_roi = True

            else:

                if type(border_width) == str:
                    border_width = int(border_width)
                    if border_width > 0:
                        generate_roi = True
                elif type(border_width) == int:
                    if border_width > 0:
                        generate_roi = True

            if generate_roi:

                dataset = self.picasso_dataset.currentText()
                channel = self.picasso_channel.currentText()

                if dataset == "All Datasets":
                    dataset = list(self.dataset_dict.keys())[0]

                image_shape = self.dataset_dict[dataset][channel.lower()]["data"].shape

                frame_shape = image_shape[1:]

                if window_cropping:

                    border_width = int(border_width)

                    if x1 < border_width:
                        x1 = border_width
                    if y1 < border_width:
                        y1 = border_width
                    if x2 > frame_shape[1] - border_width:
                        x2 = frame_shape[1] - border_width
                    if y2 > frame_shape[0] - border_width:
                        y2 = frame_shape[0] - border_width

                    roi = [[y1, x1], [y2, x2]]

                else:

                    roi = [[int(border_width), int(border_width)],
                           [int(frame_shape[0] - border_width), int(frame_shape[1] - border_width)]]

        except:
            print(traceback.format_exc())
            pass

        return roi

    def export_picasso_locs(self, locs):

        if self.verbos:
            print("Exporting Picasso locs")

        try:

            dataset_name = self.picasso_dataset.currentText()
            image_channel = self.picasso_channel.currentText()
            min_net_gradient = int(self.picasso_min_net_gradient.text())
            box_size = int(self.picasso_box_size.currentText())

            path = self.dataset_dict[dataset_name][image_channel.lower()]["path"]
            image_shape = self.dataset_dict[dataset_name][image_channel.lower()]["data"].shape

            base, ext = os.path.splitext(path)
            path = base + f"_{image_channel}_picasso_locs.hdf5"

            info = [{"Byte Order": "<", "Data Type": "uint16", "File": path,
                     "Frames": image_shape[0], "Height": image_shape[1],
                     "Micro-Manager Acquisiton Comments": "", "Width": image_shape[2], },
                    {"Box Size": box_size, "Fit method": "LQ, Gaussian",
                     "Generated by": "Picasso Localize",
                     "Min. Net Gradient": min_net_gradient, "Pixelsize": 130, "ROI": None, }]

            from picasso.io import save_locs
            # save_locs(path, locs, info)

        except:
            print(traceback.format_exc())
            pass
