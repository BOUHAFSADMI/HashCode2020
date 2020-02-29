def solve(d, s, T, ids, profit):
    all_ids = list()
    ids_list = dict()

    i = 0
    for x in profit.keys():
        sub_ids_list = list()
        id = ids[x]

        if i + T[x] < d:
            i += T[x]

            z = [x for _, x in sorted(zip(s, id))]

            for k in z:
                if k not in all_ids:
                    all_ids.append(k)
                    sub_ids_list.append(k)
            if len(sub_ids_list) != 0:
                ids_list[x] = sub_ids_list


        else:
            break

    print(len(ids_list))
    for ii, jj in zip(ids_list.keys(), ids_list.items()):
        print(ii, len(jj[1]))



        print(*jj[1])


if __name__ == "__main__":
    # print("Starting...")

    b, l, d = input().split()

    b = int(b)  # books number
    l = int(l)  # libraries number
    d = int(d)  # days number

    s = [int(x) for x in input().split()]  # books scores

    N = list()  # the number of books in library j
    T = list()  # the number of days it takes to finish the library signup
    M = list()  # the number of books that can be shipped from library j per day
    ids = list()  # books IDs

    profit = dict()
    for x in range(0, l):
        n, t, m = input().split()

        n = int(n)
        t = int(t)
        m = int(m)

        N.append(int(n))
        T.append(int(t))
        M.append(int(m))
        id = [int(c) for c in input().split()]
        ids.append(id)

        profit[x] = m*(d - t)

    profit = {k: v for k, v in sorted(profit.items(), key=lambda item: item[1], reverse=False)}

    solve(d, s, T, ids, profit)

    # print("End...")
