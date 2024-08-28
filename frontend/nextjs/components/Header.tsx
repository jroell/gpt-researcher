import Image from "next/image";

const Header = () => {
  return (
    <div className="container h-[60px] px-4 lg:h-[80px] lg:px-0 pt-10">
      <div className="grid h-full grid-cols-12">
        <div className="col-span-5"></div>
        <div className="col-span-2 flex items-center justify-center">
          <a href="/">
            <Image
              src="/img/gptr-logo.png"
              alt="logo"
              width={1004}
              height={264}
            />
          </a>
        </div>
      </div>
    </div>
  );
};

export default Header;
