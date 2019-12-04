class GetParamsList:
    def __init__(self, percent_lists_new, repercent_lists_new):
        self.percent_lists_new = percent_lists_new
        self.repercent_lists_new = repercent_lists_new

    def get_percent_list(self):
        percent_list_new_all = []
        for i in range(len(self.percent_lists_new)):
            percent_list_new = self.percent_lists_new[i][0:1]
            for s in range(len(self.percent_lists_new[i]) - 1):
                a = self.percent_lists_new[i][s + 1] - self.percent_lists_new[i][s]
                percent_list_new.append(a)
            percent_list_new_all.append(percent_list_new)
        # print(percent_list_new_all)
        return percent_list_new_all

    def get_repercent_list(self):
        repercent_list_new_all = []
        for i in range(len(self.repercent_lists_new)):
            repercent_list_new = self.repercent_lists_new[i][0:1]
            for s in range(len(self.repercent_lists_new[i]) - 1):
                a = self.repercent_lists_new[i][s + 1] - self.repercent_lists_new[i][s]
                repercent_list_new.append(a)
            repercent_list_new_all.append(repercent_list_new)
        # print(repercent_list_new_all)
        return repercent_list_new_all


# percent_lists_new = [[5.0, 9.0, 13.0, 15.0, 17.0], [5.0, 9.0, 13.0, 15.0, 17.0], [5.0, 9.0, 13.0, 15.0, 17.0], [5.0, 9.0, 13.0, 15.0, 17.0]]
# repercent_lists_new = [[1.0, 2.0, 3.0, 4.0, 5.0], [1.0, 2.0, 3.0, 4.0, 5.0], [1.0, 2.0, 3.0, 4.0, 5.0], [1.0, 2.0, 3.0, 4.0, 5.0]]
#
#
# GetParamsList(percent_lists_new, repercent_lists_new).get_percent_list()
# GetParamsList(percent_lists_new, repercent_lists_new).get_repercent_list()