from trulens.core import TruSession
from trulens.dashboard.run import run_dashboard




def load_trulens():

    session = TruSession(database_url="postgresql://postgres:password@relational_db:5432")

    run_dashboard(session, port=8000, force=True)


if __name__ == "__main__":
    load_trulens()
