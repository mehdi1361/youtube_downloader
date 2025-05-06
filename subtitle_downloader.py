

from youtube_transcript_api import YouTubeTranscriptApi # type: ignore
from youtube_transcript_api.formatters import SRTFormatter # type: ignore


def main():
    vid_id = "KHxX0CgMGs4"
    transcripts = YouTubeTranscriptApi.list_transcripts(video_id=vid_id)
    base_lang = "en"
    want_lang = "fa"
    # print(transcripts)
    base_obj = transcripts.find_transcript([base_lang])
    base_trans = base_obj.fetch()
    fmt = SRTFormatter()
    base_txt = fmt.format_transcript(base_trans)
    print(f"Writing {base_lang} Transcript")
    
    with open(f"transcripts/{base_lang}_{vid_id}_transcript.srt", "w") as f:
        f.write(base_txt)

    print("Done!!!")
    
    if base_obj.is_translatable:
        want_trans = base_obj.translate(want_lang).fetch()
        want_txt = fmt.format_transcript(want_trans)
        print(f"Writing {base_lang} Transcript")
    
        with open(f"transcripts/{want_lang}_{vid_id}_transcript.srt", "w") as f:
            f.write(want_txt)

        
    else:
        print(f"Can not translate transcript to {want_lang}")
        quit()

    print(want_trans)
        
    
main()