file_with_old_links = open('./.data/links.txt', 'r')
file_with_new_links = open('./.data/new_links.txt', 'w')
file_with_instructor_links = open('./.data/instructor_links.txt', 'w')

for link in file_with_old_links:
    # Get the question id from the old link
    question_id = link.split('/')[-1].rstrip()

    # Build a new link with question id
    new_link = f'https://www.udemy.com/course/the-complete-javascript-course/learn/lecture/5869204#questions/{question_id}'
    instructor_link = f'https://www.udemy.com/instructor/communication/qa/{question_id}/detail/'

    # Write the new link to a file
    file_with_new_links.write(f'{new_link}\n')
    file_with_instructor_links.write(f'{instructor_link}\n')

file_with_old_links.close()
file_with_new_links.close()
file_with_instructor_links.close()