from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Platform, Base, AdProduct, User

engine = create_engine('sqlite:///PlatformAdProductwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create  user
User1 = User(name="Ann Zhou", email="bookcooklook@gmail.com",
             picture='https://i.stack.imgur.com/S8VxD.jpg?s=328&g=1')
session.add(User1)
session.commit()

############################
#### Ad product for Facebook
############################
Platform1 = Platform(name="Facebook",user_id=1)

session.add(Platform1)
session.commit()

AdProduct1 = AdProduct(user_id=1, name="Video Ads", description="Showing off product features with sound and motion", CPC="$0.5", Format="Video", Platform=Platform1)
session.add(AdProduct1)
session.commit()

AdProduct2 = AdProduct(user_id=1, name="Image Ads", description="Driving people to destination websites or apps through high-quality visuals", CPC="$0.25", Format="Image", Platform=Platform1)
session.add(AdProduct2)
session.commit()

AdProduct3 = AdProduct(user_id=1, name="Collection Ads", description="Encouraging shopping by displaying items from your product catalog - customized fro each individual", CPC="$0.29", Format="Image", Platform=Platform1)

session.add(AdProduct3)
session.commit()

AdProduct4 = AdProduct(user_id=1, name="Carousel Ads", description="Showing up to 10 images or videos within a single ad, each with its own link", CPC="$0.25", Format="Image", Platform=Platform1)

session.add(AdProduct4)
session.commit()


AdProduct5 = AdProduct(user_id=1, name="Lead Ads", description="Instead of sending users to a landing page where they will fill out a lead form on your website, Facebook leead ads allow potential users to access your offers without ever leaving the Facebook app.", CPC="$0.29", Format="All", Platform=Platform1)

session.add(AdProduct5)
session.commit()

AdProduct6 = AdProduct(user_id=1, name="Post Engagement Ads", description="Most Page posts on Facebook can be boosted to deliver more likes, comments, shares, and photo views.", CPC="$0.29", Format="All", Platform=Platform1)

session.add(AdProduct6)
session.commit()


AdProduct7 = AdProduct(user_id=1, name="Event Responses", description="Event response ads can be used to promote awareness of your event and drive responses. You can design your event ad to appear as an image or video.", CPC="$0.25", Format="All", Platform=Platform1)

session.add(AdProduct7)
session.commit()

############################
#### Ad product for Instagram
############################
Platform2 = Platform(name="Instagram",user_id=1)

session.add(Platform1)
session.commit()

AdProduct1 = AdProduct(user_id=1, name="Photo Ads", description="Tell your story through a clean, simple and beautiful creative canvas. Photos can be in square or landscape format.",
                     CPC="$0.30", Format="Image", Platform=Platform2)
session.add(AdProduct1)
session.commit()

AdProduct2 = AdProduct(user_id=1, name="Video Ads", description="Get the same visually immersive quality as photo ads with the added power of sight, sound and motion. And now, you can share videos up to 60 seconds long in landscape or square format.",
                     CPC="$0.25", Format="Video", Platform=Platform2)

session.add(AdProduct2)
session.commit()

AdProduct3 = AdProduct(user_id=1, name="Carousel Ads", description="Bring another layer of depth to campaigns where people can swipe to view additional photos or videos in a single ad.",
                     CPC="$0.29", Format="All", Platform=Platform2)

session.add(AdProduct3)
session.commit()

AdProduct4 = AdProduct(user_id=1, name="Stories Ads", description="Complement your feed content with ads on Instagram Stories. Connect with the 400M+ accounts using stories daily.1 Learn more about stories ads and specs.",
                     CPC="$0.25", Format="All", Platform=Platform2)

session.add(AdProduct4)

session.commit()
AdProduct5 = AdProduct(user_id=1, name="Collection Ads", description="You can use Collection to visually inspire and help your audience discover, browse and purchase products. Tell an integrated story with a product or lifestyle focus, through video, images or both.", CPC="$0.25", Format="All", Platform=Platform2)

session.add(AdProduct5)
session.commit()
######################
#### Ad product for Snapchat
######################

Platform3 = Platform(name="Snapchat", user_id=1)

session.add(Platform3)
session.commit()


AdProduct1 = AdProduct(user_id=1, name="Snap Ads", description="Showing Ads to usrs after a single swipe and driving users to your website, app, video, AR Lens, or app store page", CPC="$0.28", Format="All", Platform=Platform3)
session.add(AdProduct1)
session.commit()

AdProduct2 = AdProduct(user_id=1, name="Collection Ads", description="Showcasing a series of products and giving users a tappable, frictionless way to shop and buy", CPC="$0.27", Format="All", Platform=Platform3)
session.add(AdProduct2)
session.commit()

AdProduct3 = AdProduct(user_id=1, name="Story Ads", description="Drawing users into a series of Snaps with a sponsored Discover tile that lives alongside popular content tailored to their preferences", CPC="$0.35", Format="All", Platform=Platform3)
session.add(AdProduct3)
session.commit()

AdProduct4 = AdProduct(user_id=1, name="AR Lenses", description="Creating memories, interactive moments with augmented reality experiences that users can play with and send to friends", CPC="$0.24", Format="All", Platform=Platform3)
session.add(AdProduct4)
session.commit()

AdProduct5 = AdProduct(user_id=1, name="Filters", description="Taking part in users' conversations with creative overlays they can add to photo and video messages", CPC="$0.25", Format="All", Platform=Platform3)
session.add(AdProduct5)
session.commit()


#####################
### Services for Google
#####################

Platform5 = Platform(name="Google",user_id=1)

session.add(Platform5)
session.commit()


AdProduct1 = AdProduct(user_id=1, name="AdSense", description="Showing product ads on third-party websites",CPC="$0.25", Format="All", Platform=Platform5)

session.add(AdProduct1)
session.commit()

AdProduct2 = AdProduct(user_id=1, name="Giferator",
                     description="Custom Ad unit for EA Sports' Madden football video game; allowing users to create thieir own Gifs", CPC="$0.25", Format="Other", Platform=Platform5)

session.add(AdProduct2)
session.commit()

AdProduct3 = AdProduct(user_id=1, name="Product Listing Ads", description="Showing up in related searches directing users to retailers online",CPC="0.15", Format="Image", Platform=Platform5)

session.add(AdProduct3)
session.commit()


print "added ad products!"
