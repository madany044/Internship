# Class and object

class Instagram:
    def __init__(self, title, description,comments, creator_name,location):  
        self.title = title
        self.description = description
        self.likes = 0
        self.comments = []  
        self.creator_name = ""  
        self.location = ""  
        
    def display_title(self):
        print("The title of the reel is ", self.title)
        
    def display_description(self):
        print("The description of the reel is ", self.description)
        
    def display_likes(self):
        print("The likes of the reel is ", self.likes)
        
    def display_comments(self):
        print("Comments: ", self.comments)
        
    def display_creator(self):
        print("Creator: ", self.creator_name)
        
    def display_location(self):
        print("Location: ", self.location)
        
    def liked(self):
        self.likes += 1
        
    def disliked(self):
        if self.likes > 0:
            self.likes -= 1
    
    def delete_comment(self):
        # Delete the last comment from the list
        if self.comments:
            deleted_comment = self.comments.pop()
            print(f"Deleted comment: '{deleted_comment}'")
        else:
            print("No comments to delete")


reel1 = Instagram("dancing", "dancing with friends")
reel2 = Instagram("finance minister conference", "finance minister conference with friends")


reel1.comments = ["Nice!", "Great moves"]
reel2.comments = ["Informative", "Important topic"]


reel1.creator_name = "Alex"
reel1.location = "New York"
reel2.creator_name = "News Channel"
reel2.location = "Delhi"

reel1.disliked() 
reel1.liked()    
reel1.liked()     
reel2.liked()     
reel1.disliked()  


reel1.display_likes() 
reel2.display_likes()  

reel1.display_comments()
reel1.display_creator()
reel1.display_location()

reel2.display_comments()
reel2.display_creator()
reel2.display_location()

print(id(reel1))
print(id(reel2))