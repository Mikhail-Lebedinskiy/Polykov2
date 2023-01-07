def load_data(file_path):
    with open(file_path) as file:
        count_of_companies = int(file.readline())
        companies = []
        for i in range(count_of_companies):
            companies.append([int(i) for i in file.readline().split()])
    return count_of_companies, companies


def max_for_one_company(company_id, company_score, count_of_companies, companies):
    for i in range(company_id, count_of_companies):
        if companies[i][1] > company_score:
            return i - company_id + 1
    return 0


def main(file_path):
    count_of_companies, companies = load_data(file_path)
    answer = -1
    for company_id, company_score in companies:
        answer = max(answer, max_for_one_company(company_id, company_score, count_of_companies, companies))
    return answer


print(main('data/A.txt'))
print(main('data/B.txt'))
