import PageRankScore as PR
import PageRankScore_XML as PRX
import PageRankScore_Dictionnaire as PRD

if __name__ == '__main__':
    matrix = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    ]

    G = {0: [],
         1: [2],
         2: [1],
         3: [0, 1],
         4: [1, 3, 5],
         5: [1, 4],
         6: [1, 4, 7],
         7: [1, 4],
         8: [1, 4],
         9: [4],
         10: [4]}

    score = PR.page_rank_score(matrix)
    print("\nFinal PageRank Scores:", score)
    print("\n --------------------------------------------------------------------------\n")
    xml_file = 'C:/Users/Othmane/Desktop/BDSaS S3/Web Analytics/PageRank/PageRank/file.xml'
    score_xml = PRX.page_rank_score(xml_file)
    print("PageRank scores for the XML file:", score_xml)
    print("\n --------------------------------------------------------------------------\n")
    score_dict = PRD.page_rank_score(G)
    print("PageRank scores for Dictionnaire :", score_dict)
    print("\n --------------------------------------------------------------------------\n")