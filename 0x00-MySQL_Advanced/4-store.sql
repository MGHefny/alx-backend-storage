-- script that creates a trigger that decreases the quantity
CREATE TRIGGER trig_quan
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
