import React from "react";

type Props = {
  title: string;
  children: React.ReactNode;
};

const Card: React.FC<Props> = ({ title, children }) => {
  return (
    <div className="card">
      <h2>{title}</h2>
      {children}
    </div>
  );
};

export default Card;
