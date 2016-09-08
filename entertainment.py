import media
import fresh_tomatoes
toy_story = media.Movie("ToyStory",
                        "Woody and his friends.",
                        "http://img.lum.dolimg.com/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",
                        "https://www.youtube.com/watch?v=JHutd0VPkz8")
zootopia  = media.Movie("Zootopia",
                        "Love is peace.",
                        "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                        "https://www.youtube.com/watch?v=bY73vFGhSVk")
the_lobster = media.Movie("The Lobster",
                          "Find your love.",
                          "http://cdn1-www.comingsoon.net/assets/uploads/gallery/the-lobster/lobstersmall.jpg",
                          "https://www.youtube.com/watch?v=vU29VfayDMw")
the_hateful_eight = media.Movie("The Hateful Eight",
                                "No one comes up here without a damn good reason.",
                                "http://ia.media-imdb.com/images/M/MV5BMjA1MTc1NTg5NV5BMl5BanBnXkFtZTgwOTM2MDEzNzE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                                "https://www.youtube.com/watch?v=gnRbXn4-Yis")
spotlight = media.Movie("Spotlight",
                         "The truth.",
                         "http://www.impawards.com/2015/posters/spotlight.jpg",
                         "https://www.youtube.com/watch?v=56jw6tasomc")
school_of_rock = media.Movie("School of Rock",
                            "Dream of Rock and Roll",
                            "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                            "https://www.youtube.com/watch?v=3PsUJFEBC74")
inside_out = media.Movie("Inside Out",
                            "I don't wanna grow up",
                            "https://images-na.ssl-images-amazon.com/images/I/51g%2B1-GJCuL._AC_UL320_SR214,320_.jpg",
                            "https://www.youtube.com/watch?v=1HFv47QHWJU")
whiplash = media.Movie("Whiplash",
                        "Chalie Parker",
                        "http://www.impawards.com/2014/posters/whiplash_ver3.jpg",
                        "https://www.youtube.com/watch?v=aHDEZXoh4-c")
slumdog_millionaire = media.Movie("Slumdog Millionaire",
                          "All about my life",
                          "http://www.impawards.com/2008/posters/slumdog_millionaire.jpg",
                          "https://www.youtube.com/watch?v=AIzbwV7on6Q")

movies = [toy_story,zootopia,the_lobster,the_hateful_eight,spotlight,school_of_rock,inside_out,whiplash,slumdog_millionaire]
fresh_tomatoes.open_movies_page(movies)

