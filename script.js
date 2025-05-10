let tasks = JSON.parse(localStorage.getItem("tasks")) || [];

function displayTasks() {
  const list = document.getElementById("taskList");
  list.innerHTML = "";
  let completedCount = 0;

  tasks.forEach((task, index) => {
    if (task.completed) completedCount++;

    const li = document.createElement("li");
    li.className = "list-group-item d-flex justify-content-between align-items-center";

    if (task.completed) li.classList.add("completed");

    li.innerHTML = `
      <div>
        <strong>${task.text}</strong>
        <span class="badge bg-secondary ms-2">${task.category}</span>
      </div>
      <div>
        <button class="btn btn-sm btn-outline-success me-2" onclick="toggleTask(${index})">
          ${task.completed ? "Undo" : "Done"}
        </button>
        <button class="btn btn-sm btn-outline-danger" onclick="deleteTask(${index})">Delete</button>
      </div>
    `;

    list.appendChild(li);
  });

  updateProgressBar(completedCount, tasks.length);
  localStorage.setItem("tasks", JSON.stringify(tasks));
}

function addTask() {
  const input = document.getElementById("taskInput");
  const category = document.getElementById("category");

  if (input.value.trim() === "") return;

  tasks.push({
    text: input.value.trim(),
    category: category.value,
    completed: false,
  });

  input.value = "";
  displayTasks();
}

function toggleTask(index) {
  tasks[index].completed = !tasks[index].completed;
  displayTasks();
}

function deleteTask(index) {
  tasks.splice(index, 1);
  displayTasks();
}

function updateProgressBar(completed, total) {
  const bar = document.getElementById("progressBar");
  let percent = total === 0 ? 0 : Math.round((completed / total) * 100);
  bar.style.width = percent + "%";
  bar.textContent = percent + "%";
}

displayTasks();
