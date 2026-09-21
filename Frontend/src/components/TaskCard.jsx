export default function TaskCard({ task }) {
  return (
    <div className="border p-4 rounded shadow">
      <h2 className="text-lg font-bold">{task.title}</h2>
      <p>{task.description}</p>
      <span className="text-sm text-gray-500">{task.status}</span>
    </div>
  );
}
