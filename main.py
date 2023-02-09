import dotenv
import dataset

def main():
    dataset_ich = dataset.RsnaICH()
    print(dataset_ich.train_labels)


if __name__ == '__main__':
    dotenv.load_dotenv()
    main()
