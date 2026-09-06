vuodenajat = (
    "talvi",
    "talvi",
    "kevät",
    "kevät",
    "kevät",
    "kesä",
    "kesä",
    "kesä",
    "syksy",
    "syksy",
    "syksy",
    "talvi"
)

kk = int(input("Anna kuukauden numero (1-12): "))

print(f"Kuukautta {kk} vastaava vuodenaika on {vuodenajat[kk - 1]}.")