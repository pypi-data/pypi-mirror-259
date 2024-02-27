import numpy as np
import pandas as pd
import pathlib
import os
from ngmt.utils.data_classes import NGMTRecording


def load_recording(
    file_name: str | pathlib.Path,
    tracking_systems: str | list[str],
    tracked_points: str | list[str] | dict[str, str] | dict[str, list[str]],
):
    """Load a recording from the Keep Control validation study.

    Parameters
    ----------
    file_name : str | pathlib.Path
        The absolute or relative path to the data file.
    tracking_systems : str | list[str]
        A string or list of strings of tracking systems for which data are to be returned.
    tracked_points : str | list[str] | dict[str, str] | dict[str, list[str]]
        Defines for which tracked points data are to be returned.
        If a string or list of strings is provided, then these will be mapped to each requested tracking system.

    Returns
    -------
    _ : NGMTRecording
        An instance of the NGMTRecording dataclass.
    """
    # Put tracking systems in a list
    if isinstance(tracking_systems, str):
        tracking_systems = [tracking_systems]

    # Tracked points will be a dictionary mapping
    # each tracking system to a list of tracked points of interest
    if isinstance(tracked_points, str):
        tracked_points = [tracked_points]
    if isinstance(tracked_points, list):
        tracked_points = {tracksys: tracked_points for tracksys in tracking_systems}
    for k, v in tracked_points.items():
        if isinstance(v, str):
            tracked_points[k] = [v]

    # From the file_name, extract the tracking system
    search_str = "_tracksys-"
    idx_from = file_name.find(search_str) + len(search_str)
    idx_to = idx_from + file_name[idx_from:].find("_")
    current_tracksys = file_name[idx_from:idx_to]

    # Initialize the data and channels dictionaroes
    data_dict, channels_dict = {}, {}
    for tracksys in tracking_systems:
        # Set current filename
        current_file_name = file_name.replace(
            f"{search_str}{current_tracksys}", f"{search_str}{tracksys}"
        )
        if os.path.isfile(current_file_name):
            # Read the data and channels info into a pandas DataFrame
            df_data = pd.read_csv(current_file_name, header=0, sep="\t")
            df_channels = pd.read_csv(
                current_file_name.replace("_motion.tsv", "_channels.tsv"),
                header=0,
                sep="\t",
            )

            # Now select only for the tracked points of interest
            df_data = df_data.loc[
                :,
                [
                    col
                    for col in df_data.columns
                    if any(
                        [
                            tracked_point in col
                            for tracked_point in tracked_points[tracksys]
                        ]
                    )
                ],
            ]
            df_channels = df_channels[
                (df_channels["tracked_point"].isin(tracked_points[tracksys]))
            ]

            # Put data and channels in output dictionaries
            data_dict[tracksys] = df_data
            channels_dict[tracksys] = df_channels
    return NGMTRecording(data=data_dict, channels=channels_dict)
