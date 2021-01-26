words = [word for word in input("Nhap vao chuoi cua ban: ").split(",")]
print (" ".join(sorted(list(set(words)))))