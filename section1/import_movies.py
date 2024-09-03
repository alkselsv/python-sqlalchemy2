import datetime
import csv
from db import Base, Session, engine
from models import Movie


def main():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with Session() as session:
        with session.begin():
            with open("movies.csv") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        row["release_date"] = datetime.datetime.strptime(
                            row["release_date"], "%Y-%m-%d"
                        ).date()
                        row["duration"] = int(row["duration"])
                        row["rating"] = float(row["rating"])
                        movie = Movie(**row)
                        session.add(movie)
                    except ValueError as e:
                        print(f"Error processing row: {row}")
                        print(f"Error message: {str(e)}")
                        continue


if __name__ == "__main__":
    main()
