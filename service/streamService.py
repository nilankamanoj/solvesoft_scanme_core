from model.stream import Stream
from service import specificSensitivityService


def get_streams():
    streams = Stream.query.all()
    for stream in streams:
        stream.specific_sensitivities = specificSensitivityService.get_specific_sensitivities_by_stream_id(stream.id)
    return streams
