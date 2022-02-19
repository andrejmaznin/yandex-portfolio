var flag = false;

function MenuClick() {
    var menu = document.getElementById("burger-menu-opened");
    var button = document.getElementById("burger-menu")
    if (flag == false) {
        menu.style.visibility = "visible";
        button.style.borderRadius = "0 0 0 0";
        flag = true;

    } else {
        menu.style.visibility = "hidden";
        button.style.borderRadius = "0 0 18px 0";
        flag = false;
    }
}