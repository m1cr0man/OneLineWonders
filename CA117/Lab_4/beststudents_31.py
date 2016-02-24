from sys import argv, exit

def main():
    try:
        with open(argv[1], 'r') as src_file:
            scores = []
            for line in src_file:
                raw_score = line.split()
                # Try converting the score
                try:
                    raw_score[0] = int(raw_score[0])
                    scores.append(tuple([' '.join(raw_score[1:]), int(raw_score[0])]))
                except ValueError:
                    print("Invalid mark %s encountered. Skipping." % raw_score[0])

            # Get best students
            highest_score = max(scores, key=lambda x: x[1])[1]
            names = [name for name, score in scores if score == highest_score]
            print("Best student(s): %s\nBest mark: %d" % (', '.join(names), highest_score))
    except FileNotFoundError:
        print("ERROR: File not found! " + argv[1])
    except OSError:
        print("ERROR: Could not access file! " + argv[1])

main()
