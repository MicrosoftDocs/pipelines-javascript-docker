import sys

if __name__ == "__main__":
    manifestData = sys.argv[1]
    print(manifestData)
    deployer = sys.argv[2]
    manifest = manifestData.split()
    digest = manifest[0]
    creationDate = manifest[2]
    print(digest)
    print(creationDate)
