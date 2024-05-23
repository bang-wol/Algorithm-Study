n=int(input())
points=list(map(int,input().split()))

unique_points=sorted(set(points))
dict={point:index for index, point in enumerate(unique_points)}

points_list=[dict[point] for point in points]

print(' '.join(map(str, points_list)))


