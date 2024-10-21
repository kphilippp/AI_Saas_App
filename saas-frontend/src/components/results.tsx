interface ResultsProps {
  keywords: string[];
  snippet: string;
}

const Results: React.FC<ResultsProps> = (props) => {
  return (
    <div className="flex flex-col space-y-4 mt-8">
      <h2 className="text-2xl font-semibold text-gray-800">{props.snippet}</h2>
      <p className="text-gray-700">Keywords: {props.keywords.join(", ")}</p>
    </div>
  );
};

export default Results;
