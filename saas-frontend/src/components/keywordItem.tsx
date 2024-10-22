interface KeyWordItemProps {
  keyword: string;
}

const KeyWordItem: React.FC<KeyWordItemProps> = (props) => {
  return (
    <h3 className="h-fit w-fit bg-[var(--sdBg)] p-2 px-3 rounded-sm">
      #{props.keyword}
    </h3>
  );
};

export default KeyWordItem;
