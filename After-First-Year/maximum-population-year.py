class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        year_count = {}
        for person in logs:
            for year in range(person[0], person[1]):
                year_count[year] = year_count.get(year, 0) + 1

        max_pop= max(year_count.values())
        earl_year= min([year for year in year_count if year_count[year] == max_pop])

        return earl_year
            