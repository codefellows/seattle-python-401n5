import Head from 'next/head';
import { replies } from '../data';
import { useState } from 'react';
import Footer from '../components/footer.js';

const tableStyle = 'border border-gray-700';

export default function Home() {
    // const [reply, setReply] = useState('Ask me anything');
    const [answeredQuestions, setAnsweredQuestions] = useState([]);

    // function questionAskedHandler(event) {
    //     event.preventDefault();
    //     const randomReply = replies[Math.floor(Math.random() * replies.length)];
    //     setReply(randomReply);
    // }

    function questionAskedHandler(event) {
        event.preventDefault();
        const randomReply = replies[Math.floor(Math.random() * replies.length)];

        const answeredQuestion = {
            question: event.target.question.value,
            reply: randomReply,
            id: answeredQuestions.length,
        };
        console.log('answeredQuestion', answeredQuestion);
        setAnsweredQuestions([...answeredQuestions, answeredQuestion]);
    }

    function getLatestReply() {
        if (answeredQuestions.length === 0) {
            return 'Ask me anything!';
        }
        return answeredQuestions[answeredQuestions.length - 1].reply;
    }

    return (
        <div>
            <Head>
                <title>Magic 8 Ball</title>
            </Head>
            <header className="flex items-center p-4 justify-between bg-gray-500 text-gray-50">
                <h1 className="text-4xl">Magic 8 Ball</h1>
                <p> { answeredQuestions.length } questions answered</p>
            </header>
            <main>
                <form onSubmit={questionAskedHandler} className="flex w-1/2 p-2 mx-auto my-4 bg-gray-200">
                    <input name="question" className="flex-auto pl-1"/>
                    <button className="px-2 py-1 bg-gray-500 text-gray-50">Ask</button>
                </form>
                <div className="w-96 h-96 mx-auto my-4 bg-gray-900 rounded-full">
                    <div className="relative flex items-center justify-center w-48 h-48 rounded-full bg-gray-50 top-16 left-16">
                        <p className="text-xl text-center" >{ getLatestReply() }</p>
                    </div>
                </div>
                <table className="w-1/2 mx-auto my-4">
                    <thead>
                        <tr>
                            <th className={`${tableStyle} pl-2`}>No.</th>
                            <th className={`${tableStyle} pl-2`}>Question</th>
                            <th className={`${tableStyle} pl-2`}>Response</th>
                        </tr>
                    </thead>
                    <tbody>
                        {answeredQuestions.map(item =>{
                            return(<tr>
                                <td className={`${tableStyle}`}>{item.id}</td>
                                <td className={`${tableStyle}`}>{item.question}</td>
                                <td className={`${tableStyle}`}>{item.reply}</td>
                            </tr>
                            );
                        })}
                    </tbody>
                </table>
            </main>
            <Footer />
        </div>);

}
