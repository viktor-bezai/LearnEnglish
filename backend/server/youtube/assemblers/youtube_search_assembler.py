from server.youtube.assemblers.youtube_list_videos_assembler import YouTubeListVideosAssembler
from server.youtube.dtos.youtube_search_dto import YouTubeSearchDTO, YouTubeSearchPageInfoDTO


class YouTubeSearchAssembler:
    def __init__(self):
        self.youtube_list_videos_assembler = YouTubeListVideosAssembler()

    def assemble_response(self, youtube_search: dict) -> YouTubeSearchDTO:
        page_info = YouTubeSearchPageInfoDTO(
            total_results=youtube_search.get("pageInfo").get("totalResults"),
            results_per_page=youtube_search.get("pageInfo").get("resultsPerPage"),
        )
        youtube_videos = youtube_search.get("items")

        items = self.youtube_list_videos_assembler.assemble_response(youtube_videos=youtube_videos)

        return YouTubeSearchDTO(
            kind=youtube_search.get("kind"),
            etag=youtube_search.get("etag"),
            next_page_token=youtube_search.get("nextPageToken"),
            region_code=youtube_search.get("regionCode"),
            page_info=page_info,
            items=items,
        )
