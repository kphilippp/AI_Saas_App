interface FormProps {
  prompt: string;
  setPrompt: React.Dispatch<React.SetStateAction<string>>;
  handleSubmit: () => void;
}

const Form: React.FC<FormProps> = (props) => {
  return (
    <div className="flex flex-col justify-evenly items-center h-[40%] w-[450px]  bg-white p-8 rounded-lg shadow-lg">
      <h1 className="text-3xl font-bold text-gray-800">SEOptimize </h1>
      <p className="text-gray-600 text-center">
        Having a hard time thinking about keywords to help improve your brands
        SEO optimization? You've come to the right place
      </p>
      <div className="flex flex-col gap-3">
        <input
          type="text"
          placeholder="coffee"
          value={props.prompt}
          onChange={(e) => props.setPrompt(e.target.value)}
          className="text-[var(--pmText)] border border-gray-300 rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 "
        />
        <button
          onClick={props.handleSubmit}
          className="bg-[var(--sdBg)] text-white p-2 rounded-md hover:bg-blue-600 transition"
        >
          Submit
        </button>
      </div>
    </div>
  );
};

export default Form;
