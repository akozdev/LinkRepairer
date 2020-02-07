file_with_old_links = open('./.data/links.txt', 'r')
file_with_new_links = open('./.data/new_links.txt', 'w')
file_with_instructor_links = open('./.data/instructor_links.txt', 'w')

for link in file_with_old_links:

    # It's impossible to generate the link to Q&A from the deep link (no info about the course name)
    if 'deeplink' in link:
        instructor_link = link.split('/?')[0]
        file_with_instructor_links.write(f'{instructor_link}\n')
        continue

    # Get the question id from the old link
    question_id = link.split('/')[-1].rstrip()
    course_name = link.split('/')[3]

    if course_name == 'course':
        new_link = link.rstrip()
    else:
        new_link = f'https://www.udemy.com/course/{course_name}/learn/lecture/5869204#questions/{question_id}'

    instructor_link = f'https://www.udemy.com/instructor/communication/qa/{question_id}/detail/'

    # Write the new link to a file
    file_with_new_links.write(f'{new_link}\n')
    file_with_instructor_links.write(f'{instructor_link}\n')

file_with_old_links.close()
file_with_new_links.close()
file_with_instructor_links.close()