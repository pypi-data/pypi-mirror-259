from __future__ import absolute_import

from uuid import uuid4

import kognic.io.client as IOC
import kognic.io.model.scene as SceneModel
import kognic.io.model.scene.lidars_sequence as LSM
import kognic.io.model.scene.resources as ResourceModel
from kognic.io.logger import setup_logging
from kognic.io.model.scene.metadata.metadata import MetaData


def run(client: IOC.KognicIOClient, project: str, dryrun: bool = True) -> SceneModel.CreateSceneResponse:
    print("Creating Lidar Sequence Scene...")

    lidar_sensor1 = "lidar"
    metadata = MetaData(**{"location-lat": 27.986065, "location-long": 86.922623, "vehicle_id": "abg"})

    lidars_seq = LSM.LidarsSequence(
        external_id=f"lidars-seq-example-{uuid4()}",
        frames=[
            LSM.Frame(
                frame_id="1",
                relative_timestamp=0,
                point_clouds=[
                    ResourceModel.PointCloud(filename="./examples/resources/point_cloud_RFL01.las", sensor_name=lidar_sensor1),
                ],
                metadata={"dut_status": "active"},
            ),
            LSM.Frame(
                frame_id="2",
                relative_timestamp=100,
                point_clouds=[
                    ResourceModel.PointCloud(filename="./examples/resources/point_cloud_RFL02.las", sensor_name=lidar_sensor1),
                ],
                metadata={"dut_status": "active"},
            ),
        ],
        metadata=metadata,
    )
    # Add input
    return client.lidars_sequence.create(lidars_seq, project=project, dryrun=dryrun)


if __name__ == "__main__":
    setup_logging(level="INFO")
    client = IOC.KognicIOClient()

    # Project - Available via `client.project.get_projects()`
    project = "<project-identifier>"
    run(client, project)
