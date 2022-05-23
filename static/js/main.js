const parrotTemplate = document.querySelector("#parrots-template");
const favoritesTemplate = document.querySelector("#favorites-template");

const renderParrot = function (parrot) {
    const {
        id,
        title,
        img,
        price,
        birthDate,
        sizes,
        isFavorite,
        features
    } = parrot;

    const parrotRow = parrotTemplate.content.cloneNode(true);

    parrotRow.querySelector(".parrot-img").setAttribute("src", img);
    parrotRow.querySelector(".parrot-title").textContent = title;
    parrotRow.querySelector(".parrot-price").textContent = price;
    parrotRow.querySelector(".parrot-size").textContent = `${sizes.width} x ${sizes.height}`;
    parrotRow.querySelector(".parrot-date").textContent = birthDate;

    const parrotFeatures = parrotRow.querySelector(".parrot-features");
    const parrotFeature = [features.split(",")];

    parrotFeature.forEach(function (feature) {
        const createFeature = document.createElement("li");
        createFeature.className = "badge bg-primary me-1 mb-1";
        createFeature.textContent = feature;
        parrotFeatures.append(createFeature);
    })

    const parrotStar = parrotRow.querySelector("#parrot-star")
    parrotStar.className = isFavorite ? parrotStar.className = "fa-solid fa-star" : parrotStar.className = "fa fa-star-o";

    parrotRow.querySelector(".parrot-edit").setAttribute("data-id", id);
    parrotRow.querySelector(".parrot-del").setAttribute("data-id", id);
    parrotRow.querySelector(".parrot-success").setAttribute("data-id", id);

    return parrotRow;
}


const renderFavorite = function (favorite) {
    const {
        id,
        title,
        img,
        price,
        birthDate,
        sizes,
        isFavorite,
        features
    } = favorite;

    const parrotRow = favoritesTemplate.content.cloneNode(true);

    parrotRow.querySelector(".parrot-img").setAttribute("src", img);
    parrotRow.querySelector(".parrot-title").textContent = title;
    parrotRow.querySelector(".parrot-price").textContent = price;
    parrotRow.querySelector(".parrot-size").textContent = `${sizes.width} x ${sizes.height}`;
    parrotRow.querySelector(".parrot-date").textContent = birthDate;

    const parrotFeatures = parrotRow.querySelector(".parrot-features");
    const parrotFeature = [features.split(",")];

    parrotFeature.forEach(function (feature) {
        const createFeature = document.createElement("li");
        createFeature.className = "badge bg-primary me-1 mb-1";
        createFeature.textContent = feature;
        parrotFeatures.append(createFeature);
    })

    const parrotStar = parrotRow.querySelector("#parrot-star")
    parrotStar.className = isFavorite ? parrotStar.className = "fa-solid fa-star" : parrotStar.className = "fa fa-star-o";

    parrotRow.querySelector(".parrot-edit").setAttribute("data-id", id);
    parrotRow.querySelector(".parrot-del").setAttribute("data-id", id);
    parrotRow.querySelector(".parrot-success").setAttribute("data-id", id);

    return parrotRow;
}


const parrotFavorites = document.querySelector(".favorites");

const renderFavorites = function () {
    parrotFavorites.innerHTML = "";

    const parrotFragment = document.createDocumentFragment();

    favorites.forEach(function (favorite) {
        const parrotRow = renderFavorite(favorite);
        parrotFragment.append(parrotRow);
    })
    parrotFavorites.append(parrotFragment);
}

const parrotsStore = document.querySelector(".parrots-wrapper");
const parrotCount = document.querySelector(".parrot-counter");
let showingParrots = parrots.slice();

const renderParrots = function () {
    parrotsStore.innerHTML = "";

    parrotCount.textContent = `Count: ${showingParrots.length}`;

    const parrotFragment = document.createDocumentFragment();

    showingParrots.forEach(function (parrot) {
        const parrotRow = renderParrot(parrot);
        parrotFragment.append(parrotRow);
    })
    parrotsStore.append(parrotFragment);
}

renderParrots();

const addForm = document.querySelector(".add-form");
const addParrotModalEl = document.querySelector("#add-parrot-modal");
const addParrotModal = new bootstrap.Modal(addParrotModalEl);

addForm.addEventListener("submit", function (evt) {
    evt.preventDefault();

    const elements = evt.target.elements;

    const titleValue = elements.title.value;
    const imgValue = elements.img.value;
    const priceValue = elements.price.value;
    const dateValue = elements.date.value;
    const widthValue = elements.parrot_width.value;
    const heightValue = elements.parrot_height.value;
    const featuresValue = elements.features.value;

    const parrot = {
        id: Math.floor(Math.random() * 1000),
        title: titleValue,
        img: String(imgValue),
        price: priceValue,
        birthDate: dateValue,
        sizes: {
            width: widthValue,
            height: heightValue,
        },
        isFavorite: false,
        features: featuresValue
    }

    parrots.push(parrot);
    localStorage.setItem("parrots", JSON.stringify(parrots));
    showingParrots.push(parrot);

    addForm.reset();
    addParrotModal.hide();

    const parrotRow = renderParrot(parrot);
    parrotsStore.append(parrotRow);
})

const editForm = document.querySelector(".edit-form");
const editParrotModalEl = document.querySelector("#edit-parrot-modal");
const editParrotModal = new bootstrap.Modal(editParrotModalEl);

const editTitle = document.querySelector("#edit-title");
const editImg = document.querySelector("#edit-img");
const editPrice = document.querySelector("#edit-price");
const editDate = document.querySelector("#edit-date");
const editWidth = document.querySelector("#edit-parrot_width");
const editHeight = document.querySelector("#edit-parrot_height");
const editfeatures = document.querySelector("#edit-features");


parrotsStore.addEventListener("click", function (evt) {
    if (evt.target.matches(".btn-danger")) {
        const clickedItemId = +evt.target.dataset.id;

        const clickedItemIndex = parrots.findIndex(function (parrot) {
            return parrot.id === clickedItemId;
        })

        parrots.splice(clickedItemIndex, 1);
        localStorage.setItem("parrots", JSON.stringify(parrots));
        showingParrots.splice(clickedItemIndex, 1);

        renderParrots();
    } else if (evt.target.matches(".btn-secondary")) {
        const clickedId = +evt.target.dataset.id;

        const clickedItemsId = parrots.find(function (parrot) {
            return parrot.id === clickedId;
        })

        editTitle.value = clickedItemsId.title;
        editImg.value = clickedItemsId.img;
        editPrice.value = clickedItemsId.price;
        editDate.value = clickedItemsId.birthDate;
        editWidth.value = clickedItemsId.sizes.width;
        editHeight.value = clickedItemsId.sizes.height;
        editTitle.value = clickedItemsId.title;
        editfeatures.value = clickedItemsId.features;

        editForm.setAttribute("data-editing-id", clickedItemsId.id);
    } else if (evt.target.matches(".btn-success")) {
        const clickedId = +evt.target.dataset.id;

        const clickedItemIndex = parrots.findIndex(function (parrot) {
            return parrot.id === clickedId;
        })

        const clickedItemsId = parrots.find(function (parrot) {
            return parrot.id === clickedId;
        })

        if (!parrots[clickedItemIndex].isFavorite) {

            parrots[clickedItemIndex].isFavorite = true;
            clickedItemsId.isFavorite = true;

            favorites.push(clickedItemsId);
            // localStorage.setItem("favorites", JSON.stringify(favorites));

            renderFavorites();
            renderParrots();
        } else {
            parrots[clickedItemIndex].isFavorite = false;

            const clickedItemIndexs = favorites.findIndex(function (parrot) {
                return parrot.id === clickedId;
            })

            favorites.splice(clickedItemIndexs, 1);
            // localStorage.setItem("favorites", JSON.stringify(favorites));


            renderFavorites();
            renderParrots();
        }
    }
})

editForm.addEventListener("submit", function (evt) {
    evt.preventDefault();

    const editingId = +evt.target.dataset.editingId;

    const titleValue = editTitle.value;
    const imgValue = editImg.value;
    const priceValue = editPrice.value;
    const dateValue = editDate.value;
    const widthValue = editWidth.value;
    const heightValue = editHeight.value;
    const featuresValue = editfeatures.value;

    const parrot = {
        id: editingId,
        title: titleValue,
        img: String(imgValue),
        price: priceValue,
        birthDate: dateValue,
        sizes: {
            width: widthValue,
            height: heightValue,
        },
        isFavorite: false,
        features: featuresValue
    }

    const editingItemsIndexs = parrots.findIndex(function (parrot) {
        return parrot.id === editingId;
    })

    const editingItemsIndex = showingParrots.findIndex(function (parrot) {
        return parrot.id === editingId;
    })

    parrots.splice(editingItemsIndexs, 1, parrot);
    localStorage.setItem("parrots", JSON.stringify(parrots));
    showingParrots.splice(editingItemsIndex, 1, parrot);

    editForm.reset();
    editParrotModal.hide();

    renderParrots();
})

const filter = document.querySelector("#filter");

filter.addEventListener("submit", function (evt) {
    evt.preventDefault();

    const elements = evt.target.elements;

    const searchValue = elements.search.value;
    const fromValue = elements.from.value;
    const toValue = elements.to.value;

    const fromWidthValue = elements.from_width.value;
    const toWidthValue = elements.to_width.value;
    const fromHeightValue = elements.from_height.value;
    const toHeightValue = elements.to_height.value;
    const sortValue = elements.sortby.value;

    showingParrots = parrots

        .sort(function (a, b) {
            switch (sortValue) {
                case "1":
                    if (a.title.toLowerCase() > b.title.toLowerCase()) {
                        return 1
                    } else if (a.title.toLowerCase() < b.title.toLowerCase()) {
                        return -1
                    } else {
                        return 0
                    }
                case "2":
                    return b.price - a.price
                case "3":
                    return a.price - b.price
                case "4":
                    return new Date(a.birthDate).getTime() - new Date(b.birthDate).getTime()
                case "5":
                    return new Date(b.birthDate).getTime() - new Date(a.birthDate).getTime()
                default:
                    break;
            }
        })
        .filter(function (parrot) {

            const searchRegExp = new RegExp(searchValue, "gi");
            const toPriceCondition = !toValue ? true : parrot.price <= toValue;
            const toWidthCondition = !toWidthValue ? true : parrot.sizes.width <= toWidthValue;
            const toHeightCondition = !toHeightValue ? true : parrot.sizes.height <= toHeightValue;

            return parrot.price >= fromValue && parrot.title.match(searchRegExp) && toPriceCondition && toWidthCondition && parrot.sizes.width >= fromWidthValue && toHeightCondition && parrot.sizes.height >= fromHeightValue;
        })

    renderParrots();
})