class BlogPost(object):
    author_name = ""
    title = ""
    text = ""
    publication_date = ""

first_post = BlogPost()
second_post = BlogPost()
third_post = BlogPost()

first_post.author_name = "John Doe"
first_post.title = "Lorem Ipsum"
first_post.text = "Lorem ipsum dolor sit amet."
first_post.publication_date = "2000.05.04"
second_post.author_name = "Tim Urban"
second_post.title = "Wait but why"
second_post.text = "A popular long-form, stick-figure-illustrated blog about almost everything."
second_post.publication_date = "2010.10.10"
third_post.author_name = "William Turton"
third_post.title = "One Engineer Is Trying to Get IBM to Reckon With Trump"
third_post.text = "Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing."
third_post.publication_date = "2017.03.28"

print(third_post.text)