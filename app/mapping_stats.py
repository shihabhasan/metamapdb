from app.models import QueryTable, ReferenceTable

def mapping_stats():

    # refDic=dict()
    # refFile=open("reference.tsv", "r")
    #
    # for line in refFile:
    #     line=line.strip()
    #     l=line.split("\t")
    #     refID=l[0]
    #     refTaxo=l[1].replace(";", "__").split("__")
    #     # domain, phylum, taxoclass, order, family, genus, species = tuple(refTaxo[1::2])
    #     # print refID, domain, phylum, taxoclass, order, family, genus, species
    #
    #     refDic[refID]= tuple(refTaxo[1::2])
    #
    #     p = ReferenceTable(refernceid=refID, domain=refDic[refID][0], phylum=refDic[refID][1],
    #                        taxoclass=refDic[refID][2], order=refDic[refID][3],
    #                        family=refDic[refID][4], genus=refDic[refID][5], species=refDic[refID][6])
    #     p.save()
        # for k in refDic:
        #     print refDic[k][2]


    #------------------

    queryDic = dict()
    queryFile = open("query.tsv", "r")

    for line in queryFile:
        line = line.strip()
        l = line.split("\t")
        queryID = l[0]
        idVar = queryID.split("_")
        if idVar[0] == 'U':
            idx = queryID
        else:
            idx = "_".join(idVar[1:])
        # print idx
        queryTaxo = l[1].replace(";", "__").split("__")
        # domain, phylum, taxoclass, order, family, genus, species = tuple(refTaxo[1::2])
        # print refID, domain, phylum, taxoclass, order, family, genus, species

        queryDic[idx] = tuple(queryTaxo[1::2])
        p = QueryTable(queryid=idx, domain=queryDic[idx][0], phylum=queryDic[idx][1],
                           taxoclass=queryDic[idx][2], order=queryDic[idx][3],
                           family=queryDic[idx][4], genus=queryDic[idx][5], species=queryDic[idx][6])
        p.save()

    return "Taxonomy ranks names added to database"