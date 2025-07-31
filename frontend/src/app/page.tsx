"use client";

import { useEffect, useState } from "react";
import API from "./lib/api";
import { Task } from "./types";

export default function Home() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [title, setTitle] = useState("");

  const fetchTasks = async () => {
    const res = await API.get("/tasks");
    console.log(res)
    setTasks(res.data);
  };

  const createTask = async () => {
    await API.post("/tasks", { title });
    setTitle("");
    fetchTasks();
  };

  const toggleTask = async (task: Task) => {
    await API.patch(`/tasks/${task.id}`, { ...task, completed: !task.completed });
    fetchTasks();
  };

  const deleteTask = async (task: Task) => {
    await API.delete(`/tasks/${task.id}`);
    fetchTasks();
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  return (
    <main className="p-8">
      <h1 className="text-2xl font-bold mb-4">Tasks</h1>
      <input
        className="border p-2 mr-2"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <button className="bg-blue-500 text-white p-2" onClick={createTask}>
        Add Task
      </button>
      <ul className="mt-4">
        {tasks.map((task) => (
          <li key={task.id} className="flex justify-between py-2">
            <span
              style={{ textDecoration: task.completed ? "line-through" : "none" }}
              onClick={() => toggleTask(task)}
              className="cursor-pointer"
            >
              {task.title}
            </span>
            <button onClick={() => deleteTask(task)} className="text-red-500">x</button>
          </li>
        ))}
      </ul>
    </main>
  );
}
