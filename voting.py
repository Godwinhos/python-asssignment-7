"""
Voting System

Task:
- Implement a simple voting system.
- Store candidates in a dictionary { "candidate_name": vote_count }
- Allow voters (by ID) to vote only once.
- Use *args to register multiple candidates at once.
- Use **kwargs to update candidate details like party, region.


// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Candidate as a class.
- Voter as a class with has_voted flag.
- Election as a manager class.
"""

candidates = {}
voters = set()

def register_candidates(*args, **kwargs):
    """Register candidates with optional metadata.
    """
    pass

def cast_vote(voter_id, candidate):
    """Cast vote if voter has not voted before.
        after all the vote logic is completeted sucessfully,
        return: Vote casted for {candidate}.
    """
    pass

def election_result():
    """Return the winner(s)."""
    # max_votes = #add logic
    # winners = #add logic
    # return {"winners": winners, "candidates": candidates}

# Voting System

# Store candidates and voters
candidates = {}   # {"candidate_name": {"votes": int, "party": str, "region": str}}
voters = set()    # Keep track of voter IDs who already voted


# Function to register multiple candidates at once using *args
def register_candidates(*args):
    for candidate in args:
        if candidate not in candidates:
            candidates[candidate] = {"votes": 0, "party": None, "region": None}
            print(f"Candidate '{candidate}' registered.")
        else:
            print(f"Candidate '{candidate}' already exists.")


# Function to update candidate details using **kwargs
def update_candidate(candidate_name, **kwargs):
    if candidate_name in candidates:
        candidates[candidate_name].update(kwargs)
        print(f"Candidate '{candidate_name}' updated: {kwargs}")
    else:
        print(f"Candidate '{candidate_name}' not found.")


# Function for voting (one voter can only vote once)
def cast_vote(voter_id, candidate_name):
    if voter_id in voters:
        print(f"Voter {voter_id} has already voted!")
        return

    if candidate_name in candidates:
        candidates[candidate_name]["votes"] += 1
        voters.add(voter_id)
        print(f"Voter {voter_id} voted for {candidate_name}.")
    else:
        print(f"Candidate '{candidate_name}' not found.")


# Function to show results
def show_results():
    print("\n--- Voting Results ---")
    for candidate, details in candidates.items():
        print(f"{candidate} ({details['party']}, {details['region']}): {details['votes']} votes")
    print("-----------------------")


# ---------------- Demo ----------------

# Register candidates
register_candidates("Alice", "Bob", "Charlie")

# Update candidate details
update_candidate("Alice", party="Party A", region="North")
update_candidate("Bob", party="Party B", region="South")
update_candidate("Charlie", party="Party C", region="East")

# Cast votes
cast_vote("V001", "Alice")
cast_vote("V002", "Bob")
cast_vote("V003", "Alice")
cast_vote("V001", "Charlie")  # Duplicate voter, should be rejected

# Show results
show_results()

