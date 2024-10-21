interface FormProps {
  prompt: string;
  setPrompt: React.Dispatch<React.SetStateAction<string>>;
  handleSubmit: () => void;
}

const Form: React.FC<FormProps> = (props) => {
  return (
    <div className="flex flex-col space-y-4 mb-8">
      <h1 className="text-3xl font-bold text-gray-800">Saas App</h1>
      <p className="text-gray-600">Tell me what your brand is about</p>
      <input
        type="text"
        placeholder="coffee"
        value={props.prompt}
        onChange={(e) => props.setPrompt(e.target.value)}
        className="border border-gray-300 rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
      <button
        onClick={props.handleSubmit}
        className="bg-blue-500 text-white p-2 rounded-md hover:bg-blue-600 transition"
      >
        Submit
      </button>
    </div>
  );
};

export default Form;
