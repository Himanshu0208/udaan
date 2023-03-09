let adjacent;
let a;
function addMore() {
  adjacent = document.getElementById("addmore");
  a = document.createElement("input");
  a.setAttribute("type", "text");
  a.setAttribute("name", `question`);
  a.setAttribute("id", `question`);
  a.setAttribute("required", true);
  a.setAttribute(
    "placeholder",
    `Write only one question in this input feild add more for the next questions`
  );
  questions.insertBefore(a , adjacent)
}

