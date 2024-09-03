import datetime
import csv
from db import Base, Session, engine
from models import Movie, Director


def main():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with Session() as session:
        with session.begin():
            with open("movies.csv") as f:
                reader = csv.DictReader(f)
                all_director_names = {}
                for row in reader:
                    try:
                        row["release_date"] = datetime.datetime.strptime(
                            row["release_date"], "%Y-%m-%d"
                        ).date()
                        row["duration"] = int(row["duration"])
                        row["rating"] = float(row["rating"])
                        director_name = row.pop("director")
                        movie = Movie(**row)
                        if director_name not in all_director_names:
                            director = Director(name=director_name)
                            session.add(director)
                            all_director_names[director_name] = director
                        all_director_names[director_name].movies.append(movie)
                    except ValueError as e:
                        print(f"Error processing row: {row}")
                        print(f"Error message: {str(e)}")
                        continue


if __name__ == "__main__":
    main()
