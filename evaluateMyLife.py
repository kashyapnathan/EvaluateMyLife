import csv
import datetime
import random
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter


class WellBeingProductivityTracker:
    MOTIVATIONAL_QUOTES = list(set([
        "Do what you can, with what you have, where you are. – Theodore Roosevelt",
        "Believe you can and you're halfway there. – Theodore Roosevelt",
        "It does not matter how slowly you go as long as you do not stop. – Confucius",
        "Our greatest weakness lies in giving up. – Thomas A. Edison",
        "You are never too old to set another goal or to dream a new dream. – C.S. Lewis",
        "With the new day comes new strength and new thoughts. – Eleanor Roosevelt",
        "It always seems impossible until it's done. – Nelson Mandela",
        "If you can dream it, you can do it. – Walt Disney",
        "Start where you are. Use what you have. Do what you can. – Arthur Ashe",
        "The secret of getting ahead is getting started. – Mark Twain",
        "Don't watch the clock; do what it does. Keep going. – Sam Levenson",
        "Aim for the moon. If you miss, you may hit a star. – W. Clement Stone",
        "Keep your eyes on the stars, and your feet on the ground. – Theodore Roosevelt",
        "You are never too old to set another goal or to dream a new dream. – C.S. Lewis",
        "Quality is not an act, it is a habit. – Aristotle",
        "Well done is better than well said. – Benjamin Franklin",
        "With the new day comes new strength and new thoughts. – Eleanor Roosevelt",
        "It takes courage to grow up and become who you really are. – E.E. Cummings"
        "Your self-worth is determined by you. You don't have to depend on someone telling you who you are. – Beyoncé"
        "Nothing is impossible. The word itself says 'I'm possible!' – Audrey Hepburn"
        "Keep your face always toward the sunshine, and shadows will fall behind you. – Walt Whitman"
        "You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose. You're on your own. And you know what you know. And you are the guy who'll decide where to go. – Dr. Seuss"
        "Attitude is a little thing that makes a big difference. – Winston Churchill"
        "To bring about change, you must not be afraid to take the first step. We will fail when we fail to try. – Rosa Parks"
        "All our dreams can come true, if we have the courage to pursue them. – Walt Disney"
        "Don't sit down and wait for the opportunities to come. Get up and make them. – Madam C.J. Walker"
        "Champions keep playing until they get it right. – Billie Jean King"
        "I am lucky that whatever fear I have inside me, my desire to win is always stronger. – Serena Williams"
        "You are never too old to set another goal or to dream a new dream. – C.S. Lewis"
        "It is during our darkest moments that we must focus to see the light. – Aristotle"
        "Believe you can and you're halfway there. – Theodore Roosevelt"
        "Life shrinks or expands in proportion to one’s courage. – Anaïs Nin"
        "Just don't give up trying to do what you really want to do. Where there is love and inspiration, I don't think you can go wrong. – Ella Fitzgerald"
        "Try to be a rainbow in someone's cloud. – Maya Angelou"
        "If you don't like the road you're walking, start paving another one. – Dolly Parton"
        "Real change, enduring change, happens one step at a time. – Ruth Bader Ginsburg"
        "All dreams are within reach. All you have to do is keep moving towards them. – Viola Davis"
        "It is never too late to be what you might have been. – George Eliot"
        "When you put love out in the world it travels, and it can touch people and reach people in ways that we never even expected. – Laverne Cox"
        "Give light and people will find the way. – Ella Baker"
        "It always seems impossible until it's done. – Nelson Mandela"
        "Don’t count the days, make the days count. – Muhammad Ali"
        "If you risk nothing, then you risk everything. – Geena Davis"
        "Definitions belong to the definers, not the defined. – Toni Morrison"
        "When you have a dream, you've got to grab it and never let go. – Carol Burnett"
        "Never allow a person to tell you no who doesn’t have the power to say yes. – Eleanor Roosevelt"
        "When it comes to luck, you make your own. – Bruce Springsteen"
        "If you're having fun, that's when the best memories are built. – Simone Biles"
        "Failure is the condiment that gives success its flavor. – Truman Capote"
        "Hard things will happen to us. We will recover. We will learn from it. We will grow more resilient because of it. – Taylor Swift"
        "Your story is what you have, what you will always have. It is something to own. – Michelle Obama"
        "To live is the rarest thing in the world. Most people just exist. – Oscar Wilde"
        "You define beauty yourself, society doesn’t define your beauty. – Lady Gaga"
        "Optimism is a happiness magnet. If you stay positive, good things and good people will be drawn to you. – Mary Lou Retton"
        "You just gotta keep going and fighting for everything, and one day you’ll get to where you want. – Naomi Osaka"
        "If you prioritize yourself, you are going to save yourself. – Gabrielle Union"
        "No matter how far away from yourself you may have strayed, there is always a path back. You already know who you are and how to fulfill your destiny. – Oprah Winfrey"
        "A problem is a chance for you to do your best. – Duke Ellington"
        "You can’t turn back the clock. But you can wind it up again. – Bonnie Prudden"
        "When you can’t find someone to follow, you have to find a way to lead by example. – Roxane Gay"
        "There is no better compass than compassion. – Amanda Gorman"
        "Stand before the people you fear and speak your mind – even if your voice shakes. – Maggie Kuhn"
        "It’s a toxic desire to try to be perfect. I realized later in life that the challenge is not to be perfect. It’s to be whole. – Jane Fonda"
        "Vitality shows not only in the ability to persist but in the ability to start over. – F. Scott Fitzgerald"
        "The most common way people give up their power is by thinking they don’t have any. – Alice Walker"
        "Love yourself first and everything else falls into line. – Lucille Ball"
        "In three words I can sum up everything I've learned about life: It goes on. – Robert Frost"
    ]))

    def __init__(self, filename='tracker_data.csv'):
        self.filename = filename
        self.ensure_file_exists()

    def ensure_file_exists(self):
        try:
            pd.read_csv(self.filename)
        except FileNotFoundError:
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Date', 'WellBeingScore',
                                'ProductivityScore', 'Comments'])

    def add_entry(self, wellbeing_score, productivity_score, comment):
        date = datetime.date.today().isoformat()
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(
                [date, wellbeing_score, productivity_score, comment])

    def read_data(self):
        return pd.read_csv(self.filename, parse_dates=['Date'])

    def plot_scores(self):
        data = self.read_data()
        fig, ax = plt.subplots(figsize=(12, 6))

        ax.plot(data['Date'], data['WellBeingScore'],
                label='Well-Being Score', marker='o', color='blue')
        ax.plot(data['Date'], data['ProductivityScore'],
                label='Productivity Score', marker='x', color='green')

        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Scores', fontsize=12)
        ax.set_title(
            'Well-Being and Productivity Scores Over Time', fontsize=14)
        ax.legend()

        date_form = DateFormatter("%m-%d")
        ax.xaxis.set_major_formatter(date_form)
        ax.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def color_text(text, color_code):
        return f"\033[{color_code}m{text}\033[0m"

    def display_tree_art(self):
        print("""
                 &&& &&  & &&
      && &\/&\|& ()|/ @, &&
      &\/(/&/&||/& /_/)_&/_&
   &() &\/&|()|/&\/ '%" & ()
  &_\_&&_\ |& |&&/&__%_/_& &&
&&   && & &| &| /& & % ()& /&&
 ()&_---()&\&\|&&-&&--%---()~
     &&     \|||
             |||
             |||
             |||
       , -=-~  .-^- _

        """)

    def display_motivational_quote(self):
        print(WellBeingProductivityTracker.color_text(
            "\nYour Motivational Quote of the Day:", "36"))
        print(WellBeingProductivityTracker.color_text(
            random.choice(self.MOTIVATIONAL_QUOTES), "33"))

        self.display_tree_art()

    def run(self):
        self.display_motivational_quote()
        while True:
            print("\nWell-Being and Productivity Tracker")
            print("1. Enter Today's Scores")
            print("2. Show Graph")
            print("3. Exit")
            choice = input("Enter choice: ")

            if choice == '1':
                wellbeing_score = input(
                    "Enter your well-being score (0-100): ")
                productivity_score = input(
                    "Enter your productivity score (0-100): ")
                comment = input("Any comments for today? (Optional): ")
                self.add_entry(wellbeing_score, productivity_score, comment)

            elif choice == '2':
                self.plot_scores()

            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    tracker = WellBeingProductivityTracker()
    tracker.run()
