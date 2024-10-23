from Musicer.playback.file_types import FileInterface, MP3, WAV, FLAC

class MusicPlayerFactory:
    @staticmethod
    def create_music_file(format_type: str) -> FileInterface:
        # Convert to lower case (no-case-sensitivity)
        format = format_type.lower()
        # Return just specified FileType Instance
        if format == "mp3":
            return MP3()
        elif format == "wav":
            return WAV()
        elif format == "flac":
            return FLAC()
        else:
            raise TypeError(f"Unsupported format: {format}")