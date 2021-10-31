import "./styles.css";

export default function App() {
  const text = 'one' in this.state ? this.state.text : this.props.text;
  return (
    <div className="App">
      <h1>Hello New React Project</h1>
      <h2>Writing React Code</h2>
      <textarea value={text} onChange={event => this.onTextChange(event)} />
      <p>{text.length}</p>
    </div>
  );
}
