class InstagramAccount:

    def __init__(self, account_name, password):
        self.account_name = account_name              
        self._private_reels = []                     
        self.__archived_reels = []                   
        self.__password = password                   

    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)

    def display_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:", self._private_reels)
        else:
            print("Access Denied! Only followers can view private reels")

    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)

    def display_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reels:", self.__archived_reels)
        else:
            print("Access Denied! Only account holder can view archived reels")

    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            return "Access Denied!"

    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password Updated Successfully")
        else:
            print("Incorrect Old Password")

account1 = InstagramAccount("madan_official", "1234")

account1.add_private_reel("Trip Reel")
account1.add_private_reel("Gym Reel")

account1.add_archived_reel("Old College Reel")
account1.add_archived_reel("School Memories")

print("\nFollower View:")
account1.display_private_reels(True)

print("\nNon-Follower View:")
account1.display_private_reels(False)

print("\nArchived Reels (Wrong Password):")
account1.display_archived_reels("0000")

print("\nArchived Reels (Correct Password):")
account1.display_archived_reels("1234")

print("\nUpdating Password:")
account1.set_password("1234", "5678")

print("\nChecking Archived Reels with New Password:")
account1.display_archived_reels("5678")
