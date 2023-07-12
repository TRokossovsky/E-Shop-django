function toggleVisibility_about() {
    let elements = document.getElementsByClassName("company-text");
    let element = elements[0];
    let element2 = elements[1];
    let frame = document.getElementById("nav-content")
    if (element.style.display === "none") {
      element.style.display = "block";
      element2.style.display = "block";
      frame.style.visibility = "visible";
    } else {
      element.style.display = "none";
      element2.style.display = "none";
      frame.style.visibility = "hidden";
    }
}
