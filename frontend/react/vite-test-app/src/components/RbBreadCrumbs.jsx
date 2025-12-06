import Breadcrumb from "react-bootstrap/Breadcrumb";
import { Link, useLocation } from "react-router-dom";
import { ArrowRight, ChevronDoubleRight, ChevronRight } from "react-bootstrap-icons";

const RbBreadCrumb = () => {
  const location = useLocation();
  const pathParts = location.pathname.split("/").filter(Boolean);

  const breadcrumbs = [
    { name: "Home", path: "/" }, ...pathParts.map((part, index) => {
      const path = "/" + pathParts.slice(0, index + 1).join("/");
      const name = part.charAt(0).toUpperCase() + part.slice(1);
      return { name, path };
    }),
  ];

  return (
    <nav aria-label="breadcrumb">
      <ol className="breadcrumb mb-3">
        {breadcrumbs.map((crumb, index) => {
          const isLast = index === breadcrumbs.length - 1;

          return (
            <li key={index} className={`breadcrumb-item ${isLast ? "active" : ""}`}>
              {!isLast ? (
                <>
                  <Link to={crumb.path}>{crumb.name}</Link>
                  <ArrowRight className="mx-2" size={14} />
                </>
              ) : (
                crumb.name
              )}
            </li>
          );
        })}
      </ol>
    </nav>
  );
};

export default RbBreadCrumb;
