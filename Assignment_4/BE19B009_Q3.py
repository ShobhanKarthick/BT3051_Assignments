import networkx as nx
import matplotlib.pyplot as plt
# Use of any function from networkx.algorithms module is strictly not allowed.
# Other libraries are not allowed expect for matplotlib for visualization purposes

# Add your functions here if needed


def planning_your_program(prerequisite_dict):
    """
    Given a dictionary of prerequisite courses, return the list of courses such that the sequence denotes the order in which the courses could possibly be done in order to satisfy the prerequisite condition.
    """
    
    """ Add your functions here if needed """
    
    def create_dependency_graph(prerequisite_dict):
        """Create and return a networkx dependency graph based on the prerequisite dictionary"""
        G = nx.DiGraph()
        for course in prerequisite_dict:
            G.add_node(course, prereqs=len(prerequisite_dict[course]))   # Add course nodes
            for prereq in prerequisite_dict[course]:
                G.add_edge(prereq, course)              # Add edges between a course and its prerequisites

        nx.draw(G, with_labels=True)
        plt.show()
        
        return G
    
    def find_the_program_pathway(G):
        """return the required program pathway from the Course Dependency Graph"""
        course_list = []
        all_courses = list(G.nodes)                     # Set of all courses that have to be completed
        while len(all_courses) != 0:
            for course in all_courses:
                neighbors = list(G.predecessors(course))    # Get all the prereqs for that course
                if len(neighbors) == 0:
                    course_list.append(course)          # Add to couse_list if course has no prereqs
                    all_courses.remove(course)
                    continue
                if all([x in course_list for x in neighbors]):      # Else, check if all the prereqs are done
                    course_list.append(course)                  # If all the pereqs are done add the course to course_list
                    all_courses.remove(course)
                    continue
                else:
                    continue

        return course_list 
    
    Course_Dependency_Graph = create_dependency_graph(prerequisite_dict)
    program_pathway = find_the_program_pathway(Course_Dependency_Graph)
    return program_pathway
    

prerequisite_dict = {"BT3051":["CS1100", "BT1000"], "CS6024":["BT3051"], "CS6091": ["CS6024", "BT3051", "CS1100"], "CS1100":[], "BT1000":[]}

print(planning_your_program(prerequisite_dict))
# Expected output: ["BT1000", "CS1100", "BT3051", "CS6024", "CS6091"] or ["CS1100", "BT1000", "BT3051", "CS6024", "CS6091"]

"""
Hints:
1. Firstly, complete all the courses that do not have any prerequisities. 
2. Then check if the first neighbors of the previous courses have prerequisities other than already completed courses. If not, then mark them complete.
3. Reinterate the 2nd step until all the courses are completed.
"""
