import Image from "next/image";
import Link from "next/link";
import Modal from './Settings/Modal';

const Footer = ({ setChatBoxSettings, chatBoxSettings}) => {
  
  return (
    <>
      <div className="container flex min-h-[72px] items-center justify-between border-t border-[#D2D2D2] px-4 pb-3 pt-5 lg:min-h-[72px] lg:px-0 lg:py-5">
        <Modal setChatBoxSettings={setChatBoxSettings} chatBoxSettings={chatBoxSettings} />
        <div className="text-sm text-gray-500">
            © {new Date().getFullYear()} Vurvey Researcher. All rights reserved.
<<<<<<< HEAD
        </div>
        <div className="flex items-center gap-3">
=======
>>>>>>> 6a8cb3c (fixes for running on server)
        </div>
      </div>
    </>
  );
};

export default Footer;
