# Problem

Estimation of price point an art work would most likely be sold at.

# Proposed Solution
This project was created with the intent of helping artist appraise their artwork.

In this project i have created a neural network to predict or estimate how much an art work would be sold at. You wold need basically a picture of dimesnsion 200x200 as the input to the system. Over the course of time if i get the chance i will make significant improvements to the system, because i believe the better the quality of the image provided to thye system the better the predictions will get.

The currency of appraisal is in euros. It works in a similar way to most of the image recognition systems however in this case I am hoping the A.i is able to identify similarities between images of diffrent artist that have the same price and estimate how much another image would be sold for. The categories in this case are spicific, there are 742 categories each representing diffrent price point as seen in the price folder. The neural network was trained om over 5,000 images of diffrent artwork although a large constituent of these are paintings.

The finished product for this project is to be a windows, .exe file, an android and iOS app. The hackathon for which this project is made is coming to an end in 7 days so i am a little bit rushed and i might only be able to make the neural net. 

**More Additions to this file wiill be made over the course of creating this project**


# Proposed Stack

- Python
- Flutter

# Benefits

- Provision of an appraisal app to help artist appraise their works.
- Creation of an art inclined A.I system.


#   Proposed directory layout

    .
    ├── prices                  # Dataset Samples
    ├── public                  # Compiled Neural Network
    ├── src                     # Source files (alternatively `lib` or `app`)
    └── README.md               # information and Instructions of Use


# How to setup project and run locally
You will need the following to run the neural net script for infrence
- Tensorflow
- Open CV
- numpy

### Clone the repository 

```
https://github.com/mrnninster/painter.gitt
```


