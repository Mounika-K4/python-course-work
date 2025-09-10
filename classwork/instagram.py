# Base Class - Instagram Story
class InstagramStory:
    def __init__(self, user):
        self.user = user
        self.story_content = ""
        super().__init__()  # Safe in case of multiple inheritance

    def post_story(self, content):
        self.story_content = content
        return f"{self.user} posted a story: {content}"

# Single Inheritance - Adds Like Feature
class StoryWithLikes(InstagramStory):
    def __init__(self, user):
        super().__init__(user)
        self.likes = 0

    def like_story(self):
        self.likes += 1
        return f"Story liked! Total likes: {self.likes}"

# Single Inheritance - Adds Comments Feature
class StoryWithComments(InstagramStory):
    def __init__(self, user):
        super().__init__(user)
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)
        return f"New comment added: {comment}"

# Hierarchical Inheritance - Adds Reaction Feature
class StoryWithReactions(InstagramStory):
    def __init__(self, user):
        super().__init__(user)
        self.reactions = {"😂": 0, "❤": 0, "🔥": 0}

    def react_to_story(self, reaction):
        if reaction in self.reactions:
            self.reactions[reaction] += 1
            return f"Reaction {reaction} added! Total: {self.reactions[reaction]}"
        else:
            return "Invalid reaction!"

# Multiple Inheritance - Combines Features
class StoryWithCloseFriends(StoryWithLikes, StoryWithComments, StoryWithReactions):
    def __init__(self, user):
        super().__init__(user)  # Calls in MRO order
        self.close_friends_only = False

    def set_close_friends(self, status):
        self.close_friends_only = status
        mode = "Close Friends" if status else "Public"
        return f"Story visibility set to: {mode}"


# Test
mouni = StoryWithCloseFriends("mouni")
print(mouni.post_story("good morning"))
print(mouni.like_story())
print(mouni.like_story())
print(mouni.add_comment("Jai mahi"))
print(mouni.react_to_story("❤"))
print(mouni.set_close_friends(True))
print(mouni.likes,mouni.comments, mouni.reactions,mouni.close_friends_only) 