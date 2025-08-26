class Drama:

    def __init__(self, name, rating, actors,
                 viewship_rate, genre, director,
                 writer, year, nr_of_episodes, network):

        self.name = name
        self.rating = rating
        self.actors = set(actors)
        self.viewship_rate = viewship_rate
        self.genre = genre
        self.director = director
        self.writer = writer
        self.year = year
        self.nr_of_episodes = nr_of_episodes
        self.network = network

    def __str__(self):
        return self.name

    def __lt__(self, other):
        if (self.rating < other.rating):
            return True
        else:
            return False

    def __repr__(self):
        return (f"{self.name} "
                f"{self.rating} "
                f"{self.actors} "
                f"{self.viewship_rate} "
                f"{self.genre} "
                f"{self.director} "
                f"{self.writer} "
                f"{self.year} "
                f"{self.nr_of_episodes} "
                f"{self.network} ")

    def add_episode(self, new_rating, actors_in_episode):
            self.nr_of_episodes += 1
            self.rating = new_rating
            self.actors.update(set(actors_in_episode))