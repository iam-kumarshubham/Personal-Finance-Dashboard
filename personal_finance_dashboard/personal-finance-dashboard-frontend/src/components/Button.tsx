import React from "react";

type Props = {
  text: string;
  variant?: "primary" | "secondary";
  onClick?: () => void;
};

const Button: React.FC<Props> = ({ text, variant = "primary", onClick }) => {
  return (
    <button className={`btn ${variant === "primary" ? "btn-primary" : "btn-secondary"}`} onClick={onClick}>
      {text}
    </button>
  );
};

export default Button;
