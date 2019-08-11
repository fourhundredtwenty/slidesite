import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension
import pynamodb


class Question:
    q_id = None
    title = ""
    _answers = []
    category = 0
    _content = ""

    def render_m(self, raw_md):
        rendered_html = markdown.markdown(
            raw_md,
            extensions=["codehilite", "sane_lists", GithubFlavoredMarkdownExtension()],
        )
        print(raw_md)
        print(rendered_html)
        return rendered_html

    # renders content to markdown
    @property
    def content(self):
        return self.render_m(self._content)

    @content.setter
    def content(self, content):
        self._content = content

    @property
    def answers(self):
        return [self.render_m(answer) for answer in self._answers]

    @answers.setter
    def answers(self, answers):
        self._answers = answers
